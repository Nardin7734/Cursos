import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

class Curso {
    private String nome;
    private int alunos;

    public Curso(String nome, int alunos) {
        this.nome = nome;
        this.alunos = alunos;
    }

    public String getNome() {
        return nome;
    }

    public int getAlunos() {
        return alunos;
    }
}

public class ExemploCursos
{
	public static void main( String[] args )
	{
		List<Curso> cursos = new ArrayList<>();
		cursos.add( new Curso( "Python", 45 ) );
		cursos.add( new Curso( "Java", 445 ) );
		cursos.add( new Curso( "JavaScript", 145 ) );
		cursos.add( new Curso( "C", 450 ) );
		
		cursos.sort( Comparator.comparing( Curso :: getAlunos ) );
		cursos.forEach( c -> System.out.println( c.getNome() ) );
		
		//Streams
		System.out.println( "Usando stream para filtrar uma collection, "
				+ "e passar pelos elementos imprimindo os seus nomes." );
		cursos.stream().filter( c -> c.getAlunos() >= 100 )
			.forEach( c -> System.out.println( c.getNome() ) );
		System.out.println("");
		
		System.out.println( "Usando stream para filtrar uma collection, "
				+ "e passar pelos elementos imprimindo uma representação numérica deles, no caso o número de alunos" );
		cursos.stream()
			.filter( c -> c.getAlunos() >= 100 )
			.map( Curso :: getAlunos )
			.forEach( System.out :: println );
		System.out.println("");
		
		//Streams e Optionals to Collection
		System.out.println( "Usando streams e Optionals" );
		Optional<Curso> optional = cursos.stream()
				.filter( c -> c.getAlunos() > 100 )
				.findAny();
		
		optional.ifPresent( c -> System.out.println( c.getNome() ) );
		List<Curso> newCursos = cursos.stream()
				.filter( c -> c.getAlunos() > 100 )
				.collect( Collectors.toList() );
		
		cursos.stream()
				.filter( c -> c.getAlunos() > 100 )
				.collect( Collectors.toMap( c -> c.getNome(), c -> c.getAlunos() ) )
				.forEach( ( nome, alunos ) -> System.out.println( nome + " tem " + alunos + " alunos."));
		
		
	}
}