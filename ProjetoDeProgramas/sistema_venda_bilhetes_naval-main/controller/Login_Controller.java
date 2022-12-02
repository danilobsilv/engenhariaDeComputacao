/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import view.Destinos;
import view.Login;
import view.Register;
import view.Login_Funcionario;

/**
 *
 * @author PauloR
 */
public class Login_Controller {

    private final Login view;

    public Login_Controller(Login view) {
        this.view = view;
    }
    
    public void goRegisterScreen(){
        Register cadastro = new Register();
        cadastro.setVisible(true);
        this.view.dispose();
    }
    
    public void goDestinosScreen(){
        Destinos destinos = new Destinos();
        destinos.setVisible(true);
        this.view.dispose();
    }
    public void goFuncionariosScreen(){
        Login_Funcionario funcionario = new Login_Funcionario();
        funcionario.setVisible(true);
        this.view.dispose();
    }
    
    public void fiz(){
        System.out.println("smsak");
        this.view.exibeMensagem("Executei");
       }
    
}
