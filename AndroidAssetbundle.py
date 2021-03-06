# coding:utf-8

import unity_tools
from os.path import join    

unity_tools.init("android_fc_win.json")

tasks = []

tasks.append(unity_tools.svn_update)

tasks.append(lambda : unity_tools.set_build_number(62))
tasks.append(lambda : unity_tools.set_version_code("6.0.0.1"))

# language bytes
# tasks.append(lambda : unity_tools.execute_unity("Editor.LanguageEditor.DownloadLanguageBytes"))
# tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "Etc", "language.bytes"), "languagebytesForClient", False))
# tasks.append(lambda : unity_tools.svn_update_by_path(unity_tools.config["serverConfigPath"]))
# tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["serverConfigPath"], "language.bytes"), "languagebytessForServer",False))

# config bytes
tasks.append(lambda : unity_tools.execute_unity("GPDataconvert.GPDataconvertEditor.UpdateInToolsBatchmode"))
tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "StaticAssets", "ConfigBytes"), "ConfigBytes", True))
tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "StaticAssets", "ConfigJsons"), "ConfigJsons", True))
tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Hot", "src", "HotConfigBean_Auto"), "HotConfigBean_Auto", True))
tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Hot", "src", "HotMes_Auto"), "HotMes_Auto", True))


# # hotfix dll
# tasks.append(lambda : unity_tools.build_hot_dll())
# tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "StaticAssets", "ILAssembly"), "ILAssembly", True))

# tasks.append(lambda: unity_tools.execute_apply_build_config("Firebase.asset"))

# tasks.append(lambda : unity_tools.execute_unity("wxbGenHotfixDegleng.DeleteCode"))
# tasks.append(unity_tools.execute_update_asset_config)
# tasks.append(lambda : unity_tools.execute_unity("wxb.GenHotfixDegleng.OnekeyGenFinal"))

tasks.append(unity_tools.execute_update_assetbundle)
# tasks.append(unity_tools.execute_fully_update_assetbundle)

# tasks.append(unity_tools.commitAssetBundles)

tasks.append(unity_tools.execute_archieve_assetbundle)

tasks.append(unity_tools.execute_upload_patch)

tasks.append(unity_tools.execute_upload_pending_version)
# tasks = []

tasks.append(unity_tools.execute_upload_version)
# tasks = []
unity_tools.do_tasks(tasks)
