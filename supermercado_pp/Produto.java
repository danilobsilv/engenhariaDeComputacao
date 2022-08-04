package supermercado_pp;

public class Produto {
    private String nome;
    private float preco;
    private int qtdeEstoque;

    public Produto(String nome, float preco, int qtdeEstoque){
        this.nome = nome;
        this.preco = preco;
        this.qtdeEstoque = qtdeEstoque;
    }

    public float getPreco() {
        return preco;
    }

    public void setPreco(float preco) {
        this.preco = preco;
    }

    public int getQtdeEstoque() {
        return qtdeEstoque;
    }

    public void setQtdeEstoque(int qtdeEstoque) {
        this.qtdeEstoque = qtdeEstoque;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
}
