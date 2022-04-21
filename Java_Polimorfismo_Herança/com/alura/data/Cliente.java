package com.alura.data;
import com.alura.util.AutenticacaoUtil;

public class Cliente implements Autenticavel
{

    private String nome;
    private String cpf;
    private String profissao;
    private AutenticacaoUtil util;
    
    public Cliente()
    {
    	this.util = new AutenticacaoUtil();
    }

    public String getNome()
    {
        return nome;
    }
    public void setNome(String nome)
    {
        this.nome = nome;
    }
    public String getCpf()
    {
        return cpf;
    }
    public void setCpf(String cpf)
    {
        this.cpf = cpf;
    }
    public String getProfissao()
    {
        return profissao;
    }
    public void setProfissao(String profissao)
    {
        this.profissao = profissao;
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