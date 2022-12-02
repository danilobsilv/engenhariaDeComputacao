/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import view.Agendamento;
import view.Pagamento;

/**
 *
 * @author PauloR
 */
public class Agendamento_Controller {
    private final Agendamento view;
    public Agendamento_Controller(Agendamento view){
        this.view = view;
    }
    
    public void goPagamentoScreen(){
        Pagamento pagamento = new Pagamento();
        pagamento.setVisible(true);
        this.view.dispose();
        
        
    }
}
