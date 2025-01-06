import requests
import csv

# Token de acesso pessoal do GitHub
GITHUB_TOKEN = "SEU_TOKEN_AQUI"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def search_repositories(per_page=100):
    """Busca os repositórios mais comentados no GitHub."""
    url = "https://api.github.com/search/issues"
    params = {
        "q": "type:pr",  # Busca apenas pull requests
        "sort": "comments",
        "order": "desc",
        "per_page": per_page
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Erro ao buscar repositórios: {response.status_code}")
        return []

def get_avg_comments(owner, repo):
    """Calcula a média de comentários por PR para um repositório."""
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    params = {"state": "all", "per_page": 100}
    page = 1
    total_comments = 0
    total_prs = 0

    while True:
        params["page"] = page
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"Erro ao buscar PRs de {owner}/{repo}: {response.json()}")
            break

        prs = response.json()
        if not prs:
            break

        for pr in prs:
            total_comments += pr.get("comments", 0)
            total_prs += 1

        page += 1

    if total_prs == 0:
        return 0
    return total_comments / total_prs

def save_to_csv(data, filename="repositories.csv"):
    """Salva os dados em um arquivo CSV."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["owner", "repository"])  # Cabeçalhos
        writer.writerows(data)

def main():
    print("Buscando repositórios mais comentados no GitHub...")
    pr_items = search_repositories()

    results = []
    for item in pr_items:
        repo_url = item["repository_url"]
        repo_details = requests.get(repo_url, headers=HEADERS).json()
        owner = repo_details["owner"]["login"]
        repo_name = repo_details["name"]
        avg_comments = get_avg_comments(owner, repo_name)
        print(f"Repositório: {owner}/{repo_name}, Média de Comentários: {avg_comments:.2f}")
        results.append([owner, repo_name])

    print("Salvando resultados em CSV...")
    save_to_csv(results)
    print("Dados salvos no arquivo repositories.csv")

if __name__ == "__main__":
    main()
