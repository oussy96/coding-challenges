import sys
from git_filter_repo import FilterRepo

def handle_commit(commit):
    commit.set_notes(b'Filtered by git-filter-repo')

    # Supprimer le secret de l'ensemble des fichiers
    if b'src/bot.py' in commit.file_changes or b'src/client.py' in commit.file_changes:
        commit.file_changes = []

    return commit

repo = FilterRepo('.', commit_callback=handle_commit)
repo.run()
