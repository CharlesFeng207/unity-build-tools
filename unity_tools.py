# coding:utf-8

import os
import sys
import json
import subprocess
from os.path import join


config = {}


def init(configName):
    with open(os.path.join(sys.path[0], configName), 'r') as f:
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


def get_svn_version():
    info = subprocess.check_output(["svnversion", config["projectPath"]])

    result = info.decode('utf-8').split(':')[-1].rstrip()
    print("get_svn_info: " + result)

    return result


def set_version_code(versionCode):
    with open(join(config["projectPath"], "TempQuickBuild",  "VersionCode.txt"), 'w') as f:
        f.write(versionCode)
    pass


def set_build_number(buildNumber):
    with open(join(config["projectPath"], "TempQuickBuild", "BuildNumber.txt"), 'w') as f:
        f.write(str(buildNumber))
    pass


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


def execute_apply_build_config(configName):
    return execute_unity("GPCommon.QuickBuild.Apply", configName)


def execute_update_asset_config():
    return execute_unity("GPCommon.AssetItemMaker.UpdateAll")


def execute_update_assetbundle():
    return execute_unity("GPCommon.AssetContainerEditor.UpdateLocal")


def execute_fully_update_assetbundle():
    return execute_unity("GPCommon.AssetContainerEditor.FullyUpdateLocal")


def execute_quick_build(configName):
    svn_version = get_svn_version()
    return execute_unity("GPCommon.QuickBuild.Build", f"{configName} {svn_version}")


def execute_unity(executeMethod, args=""):
    cmd = r"{0} -batchmode -nographics -projectPath {1} -executeMethod {2} {3} -quit -logFile executeMethod.log >> execute_unity.log".format(
        config["unityPath"], config["projectPath"], executeMethod, args)
    return print_and_run(cmd)


def svn_update():
    cmd = r"svn update {0} --username {1} --password {2} --accept tc".format(
        config["projectPath"], config["svn_username"], config["svn_password"])

    r = print_and_run(cmd)
    if r != 0:
        return print_and_run(cmd)  # try again
    return r


def commitAssetBundles():
    print_and_run(r"svn add {0}\*".format(config["assetBundlesPath"]))
    return print_and_run(r"svn commit -m \"AssetBundles\" {0} --username {1} --password {2}".
                         format(config["assetBundlesPath"], config["svn_username"], config["svn_password"]))


if __name__ == "__main__":
    init("test.json")
    get_svn_version()

    # set_version_code("2.0.0.0")
    # set_build_number(26)
    # print(svn_update())
    # print(commitAssetBundles())
    # print(execute_unity("Editor.EditorTest.TestBatchMode"))
    pass
