package com.alura.data;
import com.alura.util.AutenticacaoUtil;

public class Gerente extends Funcionario implements Autenticavel
{	
	private AutenticacaoUtil util;
    
    public Gerente()
    {
    	this.util = new AutenticacaoUtil();
    }	
	
	public double getBonificacao()
	{
		return super.getSalario() * 0.1;
	}
	
	@Override
    public boolean autentica(int senha)
    {
    	return this.util.autentica(senha);
    }
    
    @Override
    public void setSenha(int senha) {
    	this.util.setSenha( senha );
    }
	
}
