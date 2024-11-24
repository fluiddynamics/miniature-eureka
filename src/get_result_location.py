import os
def get_environment():
    if os.getenv('GITHUB_ACTIONS') == 'true':
        return "workflow"
    # pythonista = False
    # if pythonista:
    #     return "tablet"
    return "local"

dirname = f"../result/{get_environment()}"
os.makedirs(dirname,exist_ok=True)
print(dirname)