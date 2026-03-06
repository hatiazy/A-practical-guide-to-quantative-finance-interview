import os
import glob

# 获取所有md文件并按文件名排序，确保章节顺序正确
md_files = sorted(glob.glob("*.md"))
output_file = "Chapter_2_Complete.md"

with open(output_file, "w", encoding="utf-8") as outfile:
    # 在文档最开头加上 [TOC] 标记，很多编辑器会将其自动渲染为目录
    outfile.write("[TOC]\n\n") 
    
    for file in md_files:
        if file == output_file:
            continue
        with open(file, "r", encoding="utf-8") as infile:
            outfile.write(infile.read() + "\n\n---\n\n") # 用分隔线隔开各章节

print(f"合并完成！已生成 {output_file}")
