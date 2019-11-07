# coding:utf-8
import unity_tools


unity_tools.init("android_Branch.json")
# unity_tools.init("ios.json")

unity_tools.set_version_code("5.0.17.0")

tasks = []

tasks.append(unity_tools.svn_update)

tasks.append(lambda: unity_tools.execute_apply_build_config("Firebase.asset"))
# tasks.append(lambda : unity_tools.execute_unity("wxb.GenHotfixDegleng.DeleteCode"))
# tasks.append(unity_tools.execute_update_asset_config)

# tasks.append(lambda : unity_tools.execute_unity("wxb.GenHotfixDegleng.OnekeyGenFinal"))
tasks.append(unity_tools.execute_update_assetbundle)
# tasks.append(unity_tools.execute_fully_update_assetbundle)

# tasks.append(unity_tools.commitAssetBundles)

# tasks.append(unity_tools.execute_archieve_assetbundle)
# tasks.append(unity_tools.execute_upload_patch)

# tasks.append(unity_tools.execute_upload_pending_version)
# tasks.append(unity_tools.execute_upload_version)


unity_tools.do_tasks(tasks)
