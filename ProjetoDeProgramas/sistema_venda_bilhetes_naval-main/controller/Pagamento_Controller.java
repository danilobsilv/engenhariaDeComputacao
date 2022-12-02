/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import view.Pagamento;
import view.Confirmacao;

/**
 *
 * @author PauloR

 */
public class Pagamento_Controller {

    private final Pagamento view;
    public Pagamento_Controller(Pagamento view){
        this.view = view;
    }
    
    public void goConfirmacaoScreen(){
        Confirmacao confirmacao = new Confirmacao();
        confirmacao.setVisible(true);
        this.view.dispose();
    }
}
