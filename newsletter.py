#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para inserir imagens fatiadas na newsletter HTML
Lê todas as imagens da pasta /images e insere na tabela #CONTEUDO
"""

import os
import glob
import re
from pathlib import Path

def ordenacao_natural(texto):
    """
    Ordenação natural (numérica) de strings
    Ex: fatia1, fatia2, fatia10 (em vez de fatia1, fatia10, fatia2)
    """
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', texto)]

def obter_imagens(pasta_imagens='images'):
    
    extensoes_imagem = ['.png', '.jpg', '.jpeg', '.gif', '.webp']
    imagens = []
    
    if not os.path.exists(pasta_imagens):
        print(f"⚠️  Pasta '{pasta_imagens}' não encontrada!")
        return imagens
    
    # Lista todos os arquivos da pasta
    arquivos = os.listdir(pasta_imagens)
    
    for arquivo in arquivos:
        # Verifica se a extensão do arquivo está na lista (case-insensitive)
        ext = os.path.splitext(arquivo)[1].lower()
        if ext in extensoes_imagem:
            caminho = os.path.join(pasta_imagens, arquivo)
            imagens.append(caminho)
    
    # Ordena numericamente    
    imagens.sort(key=ordenacao_natural)
    
    return imagens

def gerar_html_imagens(imagens):
   
    html_linhas = []
    
    for imagem in imagens:
        # Converte para caminho com barras normais
        caminho = imagem.replace('\\', '/')
        html_linhas.append(f'<tr><td><img src="{caminho}" style="display: block; margin: 0;"/></td></tr>')
    
    return '\n'.join(html_linhas)

def inserir_imagens_no_html(arquivo_html='index.html', pasta_imagens='images'):
   
    # Verifica se o arquivo HTML existe
    if not os.path.exists(arquivo_html):
        print(f"❌ Arquivo '{arquivo_html}' não encontrado!")
        return False    
    
    imagens = obter_imagens(pasta_imagens)
    
    if not imagens:
        print(f"❌ Nenhuma imagem encontrada na pasta '{pasta_imagens}'!")
        return False
    
    print(f"✅ Encontradas {len(imagens)} imagens:")
    for img in imagens:
        print(f"   - {img}")
    
    # Gera o HTML das imagens
    html_imagens = gerar_html_imagens(imagens)
    
    # Lê o arquivo HTML
    with open(arquivo_html, 'r', encoding='utf-8') as f:
        conteudo_html = f.read()
    
    # Procura pelo marcador de conteúdo
    marcador_inicio = '<!-- CONTEUDO -->'
    marcador_fim = '<!-------------->'
    
    inicio = conteudo_html.find(marcador_inicio)
    fim = conteudo_html.find(marcador_fim)
    
    if inicio == -1 or fim == -1:
        print("❌ Marcadores de conteúdo não encontrados no HTML!")
        return False
    
    # Substitui o conteúdo entre os marcadores
    novo_conteudo = (
        conteudo_html[:inicio + len(marcador_inicio)] + 
        '\n\n' + 
        html_imagens + 
        '\n\n                  ' +
        conteudo_html[fim:]
    )
    
    # Salva o arquivo atualizado
    with open(arquivo_html, 'w', encoding='utf-8') as f:
        f.write(novo_conteudo)
    
    print(f"\n✅ Newsletter atualizada com sucesso!")
    print(f"📄 Arquivo: {arquivo_html}")
    
    return True

def main():
    """
    Função principal
    """
    print("=" * 60)
    print("   GERADOR DE NEWSLETTER - INSERIR IMAGENS FATIADAS")
    print("=" * 60)
    print()
    
    # Executa o script
    inserir_imagens_no_html()
    
    print()
    print("=" * 60)

if __name__ == "__main__":
    main()

