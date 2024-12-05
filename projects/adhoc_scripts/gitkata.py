def lskata():
    """Lists supported katas"""
    supported_katas = [
                        "Update local repo from master",
                        "One-time setup",
                        "After a PR"
                    ]
    ctr = 1
    print("Pick your kata:")
    for supported_kata in supported_katas:
        print(f"{ctr}. {supported_kata}")
        ctr += 1

def getkata(kata):
    """Displays kata"""
    if kata == 1: # update local repo from master
        update_local_repo_from_master = """
            asd
            asd
        """
        print(update_local_repo_from_master)

lskata()
pick = input('Number: ')
getkata(pick)