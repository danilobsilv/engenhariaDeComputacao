package supermercado_pp;

public class Item {
    private Produto produto;
    private int qtdeProduto;

    public Item(Produto produto, int qtdeProduto){
        this.produto = produto;
        this.qtdeProduto = qtdeProduto;
    }

    public Produto getProduto() {
        return produto;
    }

    public void setProduto(Produto produto) {
        this.produto = produto;
    }

    public int getQtdeProduto() {
        return qtdeProduto;
    }
    
    public void setQtdeProduto(int qtdeProduto) {
        this.qtdeProduto = qtdeProduto;
    }    
}
