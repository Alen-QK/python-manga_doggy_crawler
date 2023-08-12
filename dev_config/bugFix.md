1. 前端重新下载功能中，filter会导致之前已经选择的内容失效 
    >复现方式：选25，再选125，最终提交的只有125
2. ~~针对Kavita的章节扫描对特殊字符进行处理~~
    >Kavita的章节扫描存在不能正确处理“-”，“()”，以及(s|S)[0-9]+的情况。该功能会错误地将带有这些情况的章节分类为其他漫画
    >>1. 英文括号转换为中文括号
    >>2. -转换为#
    >>3. 在(s|S)与[0-9]+之间加上#
3. 缓解用户可能存在的同部漫画重复下载的问题
    >用户可能会重复下载同名漫画，此外Kavita不甚支持同名漫画同时存在多部，导致可能忽略其中一部，即无效下载
    >>漫画名查重：原名查一遍，英文大小写各查一遍，如果全部通过，直接加入队列，返回200；如果其中一个不过，那么就返回库中已有的漫画名，以及一个警示代码
4. Fate/strange fake漫画文件夹结构出现问题，Fate被独立分类为一级文件夹：Fate/strange fake$123456/Fate/strange fake/漫画内容
   >建议尝试使用该文件名测试文件名截取脚本复现