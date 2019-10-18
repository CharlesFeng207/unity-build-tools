# coding:utf-8

import unity_tools

unity_tools.init("ios.json")

unity_tools.set_build_number(40)
unity_tools.set_version_code("4.0.0.0")

tasks = []

tasks.append(unity_tools.svn_update)

tasks.append(lambda : unity_tools.execute_apply_build_config("Firebase.asset"))

# tasks.append(lambda : unity_tools.execute_unity("wxb.GenHotfixDegleng.DeleteCode"))
tasks.append(unity_tools.execute_update_asset_config)

tasks.append(lambda : unity_tools.execute_unity("wxb.GenHotfixDegleng.OnekeyGenFinal"))

tasks.append(unity_tools.execute_update_assetbundle)
# tasks.append(unity_tools.execute_fully_update_assetbundle)
tasks.append(lambda : unity_tools.execute_quick_build("Firebase.asset"))

tasks.append(unity_tools.execute_export_lastbuild_ipa)
tasks.append(unity_tools.execute_upload_lastbuild)

unity_tools.do_tasks(tasks)