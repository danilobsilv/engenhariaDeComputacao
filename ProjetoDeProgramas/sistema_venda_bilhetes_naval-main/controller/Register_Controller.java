/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import view.Login;
import view.Register;

/**
 *
 * @author PauloR
 */
public class Register_Controller {
    private final Register view;
    
    public Register_Controller(Register view) {
        this.view = view;
    }
    
    public void goLoginScreen(){
        Login login = new Login();
        login.setVisible(true);
        this.view.dispose();
                
    }
    
    
        
    
}
