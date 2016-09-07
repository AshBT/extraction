'''
Created on Mar 10, 2016

@author: bamana
'''
import os
import codecs
from learning.PageManager import PageManager

# TODO:
# sort the pages output (if possible)
# fix the ascii output bug
# (1) know if the files are ads or not in the output
# (2) use the names of the "urls" for clustering - if we can get the names

def main():

    pageManager = PageManager()
    
    ground_truth_file = '/Users/matt/Projects/memex/memexpython/Matt_Memex_Data/classified-ads-list.csv'
    ground_truth = [
                     '01A25EC49B86501FC1167A8FC367C571698028E639678A4B009D057EA4B7E68B.html'
                    ,'0B532ADFD78CE9384774D235EBDCFEDBD97B1190564758CDF80EA3B6F925F27C.html'
                    ,'0E725A334D03FF2ABD4EDC67AFF253B7C8BECD23DD91A507708AC27A0C9A5251.html'
                    ]

    page_file_dir = '/Users/bamana/Documents/InferLink/workspace/uk-hack-1/data/weapons/www.elpasoguntrader.com/test/'
    files = [f for f in os.listdir(page_file_dir) if os.path.isfile(os.path.join(page_file_dir, f))]
    count = 1
    for the_file in files:
        if the_file.startswith('.'):
            continue
        
        with codecs.open(os.path.join(page_file_dir, the_file), "r", "utf-8") as myfile:
            page_str = myfile.read().encode('utf-8')

        pageManager.addPage(format(count, '03')+'-'+the_file, page_str)
        count += 1

    (all_chunks, page_chunks_map) = pageManager.doTruffleShuffle(ground_truth)
#     
#     print all_chunks
#     
#     print ''
#     print ''
#     print ''
#     print page_chunks_map
    
    
#     test_string = ' '.join(test_string.split())
#     
#     for triple in pageManager.getVisibleTokenStructure():
#         if triple['invisible_token_buffer_before'].endswith(test_string):
#             print json.dumps(triple)
#         with codecs.open(os.path.join('/Users/bamana/Documents/InferLink/workspace/memex/memexpython/output', the_file+"_visible.txt"), "w", "utf-8") as myfile:
#             myfile.write(pageManager.getVisibleTokenBuffer(the_file))

if __name__ == '__main__':
    main()