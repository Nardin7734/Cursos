package com.alura.services;
import com.alura.data.ContaCorrente;
import com.alura.data.ContaPoupanca;

public class CriaConta {

    public static void main(String[] args) {
        ContaCorrente primeiraConta = new ContaCorrente(6646,969060);
        primeiraConta.deposita(200);
        System.out.println(primeiraConta.getSaldo());

        primeiraConta.deposita(100);
        System.out.println(primeiraConta.getSaldo());

        ContaPoupanca segundaConta = new ContaPoupanca(6645,969061);
        segundaConta.deposita(50);

        System.out.println("primeira conta tem " + primeiraConta.getSaldo());
        System.out.println("segunda conta tem " + segundaConta.getSaldo());

        System.out.println("referenciar: " + primeiraConta);
    }

}