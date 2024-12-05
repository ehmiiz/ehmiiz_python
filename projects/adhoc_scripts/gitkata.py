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
    convert_answer = int(kata)
    
    # simple kata
    yes = "asd"
    if convert_answer == 1:
        print(f"asd {yes}")

lskata()
kata = input('Number: ')
getkata(kata)