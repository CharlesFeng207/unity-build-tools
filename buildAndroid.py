# coding:utf-8

import unity_tools

unity_tools.init("android.json")
unity_tools.set_build_number(40)
unity_tools.set_version_code("4.0.0.0")

tasks = []

tasks.append(unity_tools.svn_update)
# tasks.append(lambda : unity_tools.execute_unity("wxb.GenHotfixDegleng.DeleteCode"))

tasks.append(lambda : unity_tools.execute_unity("GPCommon.QuickBuild.Apply", "Firebase.asset"))

# tasks.append(lambda : unity_tools.execute_unity("GPCommon.AssetItemMaker.UpdateAll"))
# tasks.append(lambda : unity_tools.execute_unity("wxb.GenHotfixDegleng.OnekeyGenFinal"))
# tasks.append(lambda : unity_tools.execute_unity("GPCommon.AssetContainerEditor.UpdateLocal"))
# tasks.append(lambda : unity_tools.execute_unity("GPCommon.AssetContainerEditor.FullyUpdateLocal"))
tasks.append(unity_tools.commitAssetBundles)

tasks.append(lambda : unity_tools.execute_unity("GPCommon.QuickBuild.Build", "Firebase.asset"))
tasks.append(lambda : unity_tools.execute_unity("Editor.OnekeyBuild.UploadLastBuild"))

unity_tools.do_tasks(tasks)