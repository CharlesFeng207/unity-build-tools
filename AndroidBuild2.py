# coding:utf-8

import unity_tools
from os.path import join    


unity_tools.init("android2.json")

tasks = []

tasks.append(unity_tools.svn_update)

tasks.append(lambda : unity_tools.set_build_number(55))
tasks.append(lambda : unity_tools.set_version_code("5.12.0.4"))


# # language bytes
tasks.append(lambda : unity_tools.execute_unity("Editor.LanguageEditor.DownloadLanguageBytes"))
tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "Etc", "language.bytes"), "languagebytesForClient", False))
tasks.append(lambda : unity_tools.svn_update_by_path(unity_tools.config["serverConfigPath"]))
tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["serverConfigPath"], "language.bytes"), "languagebytesForServer",False))

# tasks = []

# # config 
tasks.append(lambda : unity_tools.execute_unity("GPDataconvert.GPDataconvertEditor.UpdateInToolsBatchmode"))
tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "StaticAssets", "ConfigBytes"), "ConfigBytes", True))
tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "StaticAssets", "ConfigJsons"), "ConfigJsons", True))
tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "Etc", "GPDataconvert", "csharp"), "GPDataconvert/csharp", True))
tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Hot", "src", "HotConfigBean_Auto"), "Hot/src/HotConfigBean_Auto", True))


# # hotfix dll
tasks.append(lambda : unity_tools.build_hot_dll())
tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "StaticAssets", "ILAssembly"), "ILAssembly", True))

tasks.append(unity_tools.svn_commmit_version)

# tasks.append(lambda : unity_tools.execute_apply_build_config("FirebaseTest.asset"))
tasks.append(lambda : unity_tools.execute_apply_build_config("Firebase.asset"))

# tasks.append(lambda : unity_tools.execute_unity("wxb.GenHotfixDegleng.DeleteCode"))
tasks.append(unity_tools.execute_update_asset_config)

tasks.append(lambda : unity_tools.execute_unity("wxb.GenHotfixDegleng.OnekeyGenFinal"))

tasks.append(unity_tools.execute_update_assetbundle)
# tasks.append(unity_tools.execute_fully_update_assetbundle)
 
# tasks.append(unity_tools.commitAssetBundles)
# tasks.append(lambda : unity_tools.execute_quick_build("FirebaseTest.asset"))
tasks.append(lambda : unity_tools.execute_quick_build("Firebase.asset"))

tasks.append(unity_tools.execute_upload_lastbuild)

# tasks = []
tasks.append(unity_tools.execute_archieve_assetbundle)
tasks.append(unity_tools.execute_upload_pending_version)
tasks.append(unity_tools.execute_upload_version)

unity_tools.do_tasks(tasks)