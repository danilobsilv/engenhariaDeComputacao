/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import view.Login_Funcionario;
import view.Cadastro_Barcos;
import view.Cadastro_Rotas;
import view.Login;
import view.Registrar_Funcionario;
/**
 *
 * @author PauloR
 */
public class Login_Funcionario_Controller {
    private final Login_Funcionario view;
    
    public Login_Funcionario_Controller(Login_Funcionario view){
        this.view = view;
    }
    
    public void goCadastroBarcosScreen(){
        Cadastro_Barcos barcos = new Cadastro_Barcos();
        barcos.setVisible(true);
        this.view.dispose();
        
    }
    
    public void goCadastroRotasScreen(){
        Cadastro_Rotas rotas = new Cadastro_Rotas();
        rotas.setVisible(true);
        this.view.dispose();
        
    }
    
    public void goLoginScreen(){
        Login login = new Login();
        login.setVisible(true);
        this.view.dispose();
                
    }
    
    public void goRegisterFuncionarioScreen(){
        Registrar_Funcionario registrarF = new Registrar_Funcionario();
        registrarF.setVisible(true);
        this.view.dispose();
    }
}
