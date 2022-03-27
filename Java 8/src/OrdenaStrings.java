import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.Collections;
import java.util.Comparator;

public class OrdenaStrings
{
	public static void main( String[] args)
	{
		List<String> palavras = new ArrayList<String>();
		palavras.add( "alura online" );
		palavras.add( "editora casa do codigo" );
		palavras.add( "caelum" );
		
		//--- Ordena��o ---
		//At� o Java 7
		Comparator<String> comparador = new ComparadorPorTamanho();
		Collections.sort( palavras, comparador );
		
		//Java 8
		palavras.sort( comparador );
		
		System.out.println( "Imprimindo usando o m�todo auxiliar dentro do ArrayList" );
		System.out.println( palavras );
		System.out.println( "" );
		
		//--- Foreach ---
		//At� o java 7
		for (String s : palavras) {
			System.out.println(s);
		}
		
		//Java 8
		Consumer<String> consumidor = new ImprimeNaLinha();
		System.out.println( "Iterando pelo ArrayList com o m�todo auxiliar "
				+ "dentro do pr�prio objeto\n com um Consumer." );
		palavras.forEach( consumidor );
		System.out.println( "" );
		
		//Lambdas Java 8
		System.out.println( "Exemplos de lambdas usados em diversos m�todos auxiliares" );
		palavras.forEach( s -> System.out.println( s ) );
		palavras.sort( ( s1, s2 ) -> Integer.compare( s1.length(), s2.length() ) );
		System.out.println( "" );
		
		//Method references Java 8
		/*
		 * S�o m�todos default, que s�o est�ticos
		 * No caso abaixo, comparing � um metodo default est�tico do Comparator
		 * e pode ser utilizado com lambda
		 * Method reference � a sintaxe nova com os "::"
		 */
		System.out.println( "Imprimindo foreach usando method reference" );
		palavras.sort( Comparator.comparing( String::length ) );
		palavras.sort( Comparator.comparing( s -> s.length() ) );
		palavras.forEach(System.out::println);
		
	}

}

class ImprimeNaLinha implements Consumer<String>
{
	@Override
	public void accept( String s )
	{
		System.out.println( s );
		
	}
}

class ComparadorPorTamanho implements Comparator<String>
{
	@Override
	public int compare( String s1, String s2)
	{
		if( s1.length() < s2.length() )
			return -1;
		if( s1.length() > s2.length() )
			return 1;
		return 0;
	}
	
}