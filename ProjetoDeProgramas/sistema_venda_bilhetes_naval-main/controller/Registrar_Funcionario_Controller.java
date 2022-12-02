package controller;
import view.Login_Funcionario;
import view.Registrar_Funcionario;

/**
 *
 * @author PauloR
 */
public class Registrar_Funcionario_Controller {
    private final Registrar_Funcionario view;
    
    public Registrar_Funcionario_Controller(Registrar_Funcionario view) {
        this.view = view;
    }
    
    public void goLoginScreen(){
        Login_Funcionario login = new Login_Funcionario();
        login.setVisible(true);
        this.view.dispose();
                
    }
    
    
        
    
}

