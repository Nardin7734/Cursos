package com.alura.util;
import com.alura.data.Autenticavel;

public class AutenticacaoUtil implements Autenticavel
{
	private int senha;
	
	@Override
    public boolean autentica(int senha) {
    	return senha == this.senha ? true : false;
    }
    
    @Override
    public void setSenha(int senha) {
    	this.senha = senha;
    }

}
