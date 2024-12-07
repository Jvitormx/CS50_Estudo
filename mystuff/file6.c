#include <stdio.h>

void somaMediaDivisores (int n, int *soma, float *media);

int main(void)
{
	//declaração de variáveis
	int numero, somaMain;
	float mediaMain;

	//lendo o valor
	printf ("Entre com um numero: ");
	scanf ("%d", &numero);

	//chamando a função
	somaMediaDivisores (numero, &somaMain, &mediaMain);

	//exibindo os resultados
	printf ("\n\nSoma dos divisores de %d: %d\n", numero, somaMain);
	printf ("Media dos divisores de %d: %.1f\n", numero, mediaMain);
}

//implementação das funções
void somaMediaDivisores (int n, int *soma, float *media)
{
	//declaração de variáveis
	int i, s = 0, quant = 0;
	float m;

	//verificando os divisores de 'n'
	for (i=1;i<=n;i++)
	{
		if (n%i==0)
		{
			s += i;
			quant++;
		}
	}

	//calculando a média
	m = (float)s/quant;

	//atribuindo os resultados aos parâmetros de saída
	*soma = s;
	*media = m;
}