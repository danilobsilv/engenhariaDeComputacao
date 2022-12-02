/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;
import view.Cadastro_Rotas;
import view.Login_Funcionario;

/**
 *
 * @author PauloR
 */
public class Cadastro_Rotas_Controller {
    private final Cadastro_Rotas view;
    public Cadastro_Rotas_Controller(Cadastro_Rotas view){
        this.view = view;
    }
    public void goLoginFuncionarioScreen(){
        Login_Funcionario funcionario = new Login_Funcionario();
        funcionario.setVisible(true);
        this.view.dispose();
    }
    
}
