# coding:utf-8
import unity_tools


unity_tools.init("android.json")

tasks = []

tasks.append(unity_tools.svn_update)
tasks.append(lambda : unity_tools.execute_unity("GPCommon.AssetItemMaker.UpdateAll"))
tasks.append(lambda : unity_tools.execute_unity("GPCommon.AssetContainerEditor.UpdateLocal"))
# tasks.append(lambda : unity_tools.execute_unity("GPCommon.AssetContainerEditor.FullyUpdateLocal"))
tasks.append(unity_tools.commitAssetBundles)

unity_tools.do_tasks(tasks)