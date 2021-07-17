##from github import Github
##import os
##from pprint import pprint
##
##def git_hub():
##
##    token = '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'
##    g = Github(token)
##    print(g.get_user())
##
####    for repo_count in g.get_user().get_project():
####        print(repo_count.name)
##
##        
##    for repo in g.get_user().get_repos()[0]:
##        print('Repositori:',repo.name)
##        print(type(repo.name))
##      
##        
##
####        # repo.edit(has_wiki=False)
####        # to see all the available attributes and methods
####        #print(dir(repo))
####  
####    repo = g.get_repo("wipro-test-surya/Test_Repository")
####    contents = repo.get_contents("")
######    print(contents)
######    # adding files
######    addfiles = repo.create_file('surya.txt', 'commit','testing')
######    print(addfiles)
####    for content_file in contents:
####        print(content_file)
##
##git_hub()
##








from github import Github
import os
from pprint import pprint
token = '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'
g = Github(token)
print(g,'******')
for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
##    print(dir(repo))

repo = g.get_repo("wipro-test-surya/Test_Repository")
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)




