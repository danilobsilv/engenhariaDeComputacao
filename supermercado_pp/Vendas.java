package supermercado_pp;

import java.util.ArrayList;

public class Vendas {
    private ArrayList<Pedido> pedidosFeitos;
    
    public Vendas(ArrayList<Pedido> pedidosFeitos) {
        this.pedidosFeitos = pedidosFeitos;
    }

    public ArrayList<Pedido> getPedidosFeitos() {
        return pedidosFeitos;
    }

    public void setPedidosFeitos(ArrayList<Pedido> pedidosFeitos) {
        this.pedidosFeitos = pedidosFeitos;
    }

    public void adicionarPedido(String nome, ArrayList<Item> produtos, TiposDePagamento modoPagamento, Vendas venda){
        Pedido pedido = new Pedido(nome, produtos, modoPagamento);
        
        this.pedidosFeitos.add(pedido);
    }   
}
