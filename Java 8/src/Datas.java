import java.time.LocalDateTime;
import java.time.LocalDate;
import java.time.Month;
import java.time.Period;
import java.time.format.DateTimeFormatter;

public class Datas
{
	public static void main( String[] args )
	{
		System.out.println( "Data de hoje" );
		LocalDate hoje = LocalDate.now();
		System.out.println( hoje );
		
		System.out.println( "Operação com LocalDate" );
		LocalDate olimpiadasRio = LocalDate.of(2016, Month.JUNE, 5);
		int anos = olimpiadasRio.getYear() - hoje.getYear();
		System.out.println( anos );
		
		System.out.println( "Periodo entre hoje e as olimpiadas" );
		Period periodo = Period.between(hoje, olimpiadasRio);
		System.out.println( periodo );
		
		System.out.println( "LocalDate e Formater" );
		LocalDate proximasOlimpiadas = olimpiadasRio.plusYears( 4 );
		System.out.println( proximasOlimpiadas );
		DateTimeFormatter formatador = DateTimeFormatter.ofPattern( "dd/MM/yyyy" );
		String valorFormatado = proximasOlimpiadas.format(formatador);
		System.out.println( valorFormatado );
		
		System.out.println( "DateTime e Formatter " );
		DateTimeFormatter formatadorHoras = DateTimeFormatter.ofPattern( "dd/MM/yyyy hh:mm" );
		LocalDateTime agora = LocalDateTime.now();
		System.out.println( agora.format(formatadorHoras));
	}

}
