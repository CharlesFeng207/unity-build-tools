# coding:utf-8

import os
import sys
import json
import subprocess
from os.path import join
import qrcode
from PIL import Image
from time import sleep

config = {}


def init(configName):
    with open(os.path.join(sys.path[0], "config", configName), 'r') as f:
        global config
        config = json.load(f)
        print(config)


def do_tasks(tasks):
    for i, t in enumerate(tasks):
        while t() != 0:
            a = ""
            while a != "y":
                a = input(f"task {i} execute failed, press 'y' to retry!")

    input("tasks done!")
    pass


def make_ipa_qrcode():

    qrcodePath = config["qrcodePath"]
    build_name = get_current_build_name()

    with open(join(qrcodePath, "temp.html"), 'r', encoding='UTF-8') as f:
        htmlTemp = f.read()

    with open(join(qrcodePath, "temp.plist"), 'r', encoding='UTF-8') as f:
        plistTemp = f.read()

    with open(join(qrcodePath, f"{build_name}.html"), 'w') as f:
        f.write(htmlTemp.format(build_name))

    with open(join(qrcodePath, f"{build_name}.plist"), 'w') as f:
        f.write(plistTemp.format(config["uploadUrl"], build_name))

    qrcodeFilePath = join(qrcodePath, f"{build_name}.png")
    qrcodeUrl = "{0}/{1}".format(config["qrcodeUrl"], f"{build_name}.html")

    # print(qrcodeFile)
    # print(qrcodeUrl)

    img = qrcode.make(qrcodeUrl)
    with open(qrcodeFilePath, 'wb') as f:
        img.save(f)

    commit_qrcode_project(build_name)
    return execute_upload(qrcodeFilePath)


def commit_qrcode_project(message):
    os.chdir(config["qrcodePath"])
    os.system("git add -A")
    os.system("git commit -m {0}".format(message))
    os.system("git push")


def get_current_build_name():
    with open(join(config["projectPath"], "TempQuickBuild",  "CurrentBuildName.txt"), 'r') as f:
        return f.read()
    pass


def get_svn_version():
    info = subprocess.check_output(["svnversion", config["projectPath"]])

    result = info.decode('utf-8').split(':')[-1].rstrip()
    print("get_svn_info: " + result)

    return result


def set_version_code(versionCode):
    try:
        with open(join(config["projectPath"], "TempQuickBuild",  "VersionCode.txt"), 'w') as f:
            f.write(versionCode)
    except:
        return -1
    return 0


def set_build_number(buildNumber):
    try:
        with open(join(config["projectPath"], "TempQuickBuild", "BuildNumber.txt"), 'w') as f:
            f.write(str(buildNumber))
    except:
        return -1
    return 0


def print_and_run(cmd):
    print(cmd)
    return os.system(cmd)


def execute_upload_version():
    return execute_unity("GPCommon.VersionFlowEditor.UploadVersion")


def execute_upload_pending_version():
    return execute_unity("GPCommon.VersionFlowEditor.UploadPendingVersion")


def execute_upload_patch():
    return execute_unity("GPCommon.VersionFlowEditor.UploadPatch")


def execute_archieve_assetbundle():
    return execute_unity("GPCommon.VersionFlowEditor.ArchiveBundles")


def execute_export_lastbuild_ipa():
    return execute_unity("GPCommon.QuickBuild.ExportLastBuildIpa")


def execute_upload_lastbuild():
    return execute_unity("Editor.OnekeyBuild.UploadLastBuild")


def execute_upload(filePath):
    return execute_unity("Editor.OnekeyBuild.UploadForBatchMode", filePath)


def execute_apply_build_config(configName):
    return execute_unity("GPCommon.QuickBuild.Apply", configName)


def execute_update_asset_config():
    return execute_unity("GPCommon.AssetItemMaker.UpdateAll")


def execute_update_assetbundle():
    return execute_unity("GPCommon.AssetContainerEditor.UpdateLocal")


def execute_fully_update_assetbundle():
    return execute_unity("GPCommon.AssetContainerEditor.FullyUpdateLocal")

def push_current_version_patch():
    return execute_unity("GPCommon.AliCdnEditor.PushCurrentVersionPatch")

def execute_quick_build(configName):
    svn_version = get_svn_version()
    return execute_unity("GPCommon.QuickBuild.Build", f"{configName} {svn_version}")


def execute_unity(executeMethod, args=""):
    cmd = r"{0} -batchmode -nographics -projectPath {1} -executeMethod {2} {3} -quit -logFile executeMethod.log >> execute_unity.log".format(
        config["unityPath"], config["projectPath"], executeMethod, args)
    return print_and_run(cmd)


def svn_update():
    return svn_update_by_path(config["svnUpdatePath"])


def svn_update_by_path(p):
    cmd = r"svn update {0} --username {1} --password {2} --accept tc".format(
        p, config["svn_username"], config["svn_password"])

    r = print_and_run(cmd)
    if r != 0:
        return print_and_run(cmd)  # try again
    return r


def build_hot_dll():
    os.chdir(join(config["projectPath"], "Hot"))
    return print_and_run("build.bat")


def commitAssetBundles():
    return svn_commmit(config["assetBundlesPath"], "AssetBundles", True)


def svn_commmit_version():
    return svn_commmit(join(config["projectPath"], "TempQuickBuild",  "VersionCode.txt"), "VersionCode.txt", False)


def wait_svn_version_code(version):
    p = join(config["projectPath"], "TempQuickBuild",  "VersionCode.txt")

    while True:
        svn_update_by_path(p)
        with open(p, 'r') as f:
            c = f.read()
            print(f"expect:{version} actual:{c}")
            if c == version:
                print("go!")
                break
        print("wait...")
        sleep(10)
    pass


def svn_commmit(path, comment, folder):
    if folder:
        print_and_run(r"svn add {0}\*".format(path))
    else:
        print_and_run(r"svn add {0}".format(path))

    return print_and_run(r"svn commit -m \"{0}\" {1} --username {2} --password {3}".
                         format(comment, path, config["svn_username"], config["svn_password"]))


if __name__ == "__main__":
    init("test.json")
    wait_svn_version_code("6.0.0.0")
    # svn_commmit_version()
    # get_svn_version()
    # print(get_current_build_name())
    # make_ipa_qrcode()

    # set_version_code("2.0.0.0")
    # set_build_number(26)
    # print(svn_update())
    # print(commitAssetBundles())
    # print(execute_unity("Editor.EditorTest.TestBatchMode"))
    pass
