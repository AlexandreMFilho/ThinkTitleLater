package player;

import java.awt.Image;
import javax.swing.ImageIcon;

public class Personagem {
    /*coordenadas do personagem*/
    private int x;
    private int y;
    private int dx;
    private int dy;

    /*posição da imagem no sprite */
    private int pos;

    /*objeto imagem personagem*/
    private Image imagem;

    /*status pesonagem*/
    private boolean isVisivel;

    /*dimesoes da imagem*/
    private static final int LARGURA = 52;
    private static final int ALTURA = 62;

    public Personagem(){
      /*objeto que referencia o local da imagem do personagem*/
      ImageIcon referencia = new ImageIcon("SPRITES/main_character/1Woodcutter/Woodcutter.png");
      imagem = referencia.getImage();//Retorna imagem
      pos = 0;  //posição inicial da imagem

      /*posição incial do personagem no jogo*/
      x = 300;
      y = 500;
      isVisivel = true;
    }

    /*move a nave*/
    public void mover(){
      x += dx;
      y += dy;
    }

    /*Métodosa de acesso*/
    public void setDX(int dx){
      this.dx = dx;
    }
    public void setDY(int dy){
      this.dy = dy;
    }
    public int getX(){
      return x;
    }
    public int getY(){
      return y;
    }
    public Image getImagem(){
      return  imagem;
    }
    public int getPos(){
      return pos;
    }
    public void SetPos(int Pos){
      pos = Pos;
    }
    public int getAlt(){
      return ALTURA;
    }
    public int getLar(){
      return LARGURA;
    }
    public boolean isVisivel(){
      return isVisivel;
    }
    public void setVisivel(boolean visivel){
      isVisivel = visivel;
    }
}
