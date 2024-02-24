import polars as pl

def duplicadas(df: pl.DataFrame):
    """
    Calcula e imprime a quantidade de linhas únicas e duplicadas em um DataFrame do Polars.

    Esta função primeiramente determina o total de linhas presentes no DataFrame fornecido. Em seguida,
    utiliza o método `distinct()` para calcular o número de linhas únicas, removendo as duplicatas.
    A diferença entre o total de linhas e as linhas únicas é considerada como o número de linhas duplicadas.
    Finalmente, a função imprime a quantidade de linhas únicas e duplicadas encontradas.

    Parâmetros:
    - df (pl.DataFrame): O DataFrame do Polars sobre o qual a verificação de duplicatas será realizada.

    Retorna:
    - None. A função apenas imprime os resultados e não retorna nenhum valor.
    
    Exemplo de uso:
    >>> df = pl.DataFrame({
    >>>     "A": [1, 2, 2, 3, 3, 3],
    >>>     "B": ["a", "b", "b", "c", "c", "c"]
    >>> })
    >>> duplicadas(df)
    Quantidade de linhas únicas: 3
    Quantidade de linhas duplicadas: 3
    """
    total_linhas = df.shape[0]
    linhas_unicas = df.unique().shape[0]  
    linhas_duplicadas = total_linhas - linhas_unicas

    print(f'Quantidade de linhas únicas: {linhas_unicas}\nQuantidade de linhas duplicadas: {linhas_duplicadas}')


def nulos(df: pl.DataFrame) -> pl.DataFrame:
    """
    Calcula e retorna um resumo dos valores nulos presentes em cada coluna de um DataFrame do Polars.

    Esta função itera por todas as colunas do DataFrame fornecido, calcula a quantidade de valores nulos
    em cada uma e compila os resultados em um novo DataFrame, que inclui o nome da coluna e a contagem
    correspondente de valores nulos.

    Parâmetros:
    - df (pl.DataFrame): O DataFrame do Polars para o qual a verificação de valores nulos será realizada.

    Retorna:
    - pl.DataFrame: Um novo DataFrame contendo duas colunas: 'Column', com os nomes das colunas do DataFrame
      original, e 'Null Count', com a quantidade de valores nulos encontrados em cada coluna.

    Exemplo de uso:

    >>> df = pl.DataFrame({
    >>>     "A": [1, None, 3],
    >>>    "B": ["a", "b", None],
    >>>    "C": [None, None, None]
    >>> })
    >>> print(resumo_valores_nulos(df))
    
    """
    null_counts = [df[col].is_null().sum() for col in df.columns]
    summary_df = pl.DataFrame({
        "Colunas": df.columns,
        "Quantidade de nulos": null_counts
    })

    return summary_df