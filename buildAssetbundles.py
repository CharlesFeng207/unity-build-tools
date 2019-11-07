# coding:utf-8
import unity_tools
from os.path import join    


unity_tools.init("android.json")
# unity_tools.init("ios.json")

unity_tools.set_version_code("5.0.18.1")

tasks = []

# tasks.append(unity_tools.svn_update)

# language bytes
# tasks.append(lambda : unity_tools.execute_unity("Editor.LanguageEditor.DownloadLanguageBytes"))s
# tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "Etc", "language.bytes"), "languagebytes", False))

# # config bytes
# tasks.append(lambda : unity_tools.execute_unity("GPDataconvert.GPDataconvertEditor.UpdateInToolsBatchmode"))
# tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "StaticAssets", "ConfigBytes"), "ConfigBytes", True))
# tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "StaticAssets", "ConfigJsons"), "ConfigJsons", True))


# # hotfix dll
# tasks.append(lambda : unity_tools.build_hot_dll())
# tasks.append(lambda : unity_tools.svn_commmit(join(unity_tools.config["projectPath"], "Assets", "StaticAssets", "ILAssembly"), "ILAssembly", True))

# tasks.append(lambda: unity_tools.execute_apply_build_config("Firebase.asset"))
# tasks.append(lambda : unity_tools.execute_unity("wxb.GenHotfixDegleng.DeleteCode"))
# tasks.append(unity_tools.execute_update_asset_config)

# tasks.append(lambda : unity_tools.execute_unity("wxb.GenHotfixDegleng.OnekeyGenFinal"))
# tasks.append(unity_tools.execute_update_assetbundle)
# tasks.append(unity_tools.execute_fully_update_assetbundle)

# tasks.append(unity_tools.commitAssetBundles)

# tasks.append(unity_tools.execute_archieve_assetbundle)
# tasks.append(unity_tools.execute_upload_patch)

# tasks.append(unity_tools.execute_upload_pending_version)
# tasks.append(unity_tools.execute_upload_version)


unity_tools.do_tasks(tasks)
