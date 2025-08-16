from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="/content/drive/MyDrive/01) GreatLearning/06) Advanced MLOPS/02) Bank Churn Project/01) MLOPS/03) Deployment",     # the local folder containing your files
    repo_id="Shanmuganathan75/Bank-Customer-Churn",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
