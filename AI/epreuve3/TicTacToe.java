import java.util.ArrayList;
/*
Essayez de faire mieux qu'un IA aléatoire!

Vous pouvez commencer avec size=3, comme un vrai tic-tac-toe,
mais idéalement une taille arbitraire devrait marcher.

Sinon, vous pouvez modifier la méthode isWon() pour qu'elle soit plus
efficace (pour une valeur de size arbitraire!).
*/

class TicTacToe{

	public static void main(String[] args){
		Board b = new Board(5);
		b.play(new RandomIA(), new RandomIA());
	}

	static class RandomIA implements AI{
		public Pair play(Board b){
			return b.emptyPositions.get((int)(Math.random()*b.emptyPositions.size()));
		}
	}

	static class Board{
		int t[][];
		int size;
		int turn = 1;
		ArrayList<Pair> emptyPositions;
		String winner = "";

		Board(int size){
			t = new int[size][size];
			this.size = size;
			this.emptyPositions = new ArrayList<Pair>();
			for (int i=0;i<size;i++){
				for (int j=0;j<size;j++){
					this.emptyPositions.add(new Pair(i, j));
					t[i][j] = 0;
				}
			}
		}

		public void draw(){
			String s = "";
			for (int i=0;i<size;i++){
				for (int j=0;j<size;j++){
					if (t[i][j]==0)
						s += " ";
					else if (t[i][j]==1)
						s += "X";
					else 
						s += "O";
				}
				s += "\n";
			}
			System.out.println(s);
		}

		public void play(AI ai1, AI ai2){
			while(true){
				draw();
				if (isWon()){
					System.out.println("Et le vainqueur est: "+winner+ "!");
					break;
				}
				if (emptyPositions.size() == 0){
					System.out.println("Partie nulle!");
					break;
				}
				Pair pos;
				if (turn == 1){
					pos = ai1.play(this);
					turn = 2;
					t[pos.x][pos.y] = 1;
				}else{
					pos = ai2.play(this);
					turn = 1;
					t[pos.x][pos.y] = 2;
				}
				System.out.println("--------------");
				emptyPositions.remove(emptyPositions.indexOf(pos));
			}
		}
		public boolean isWon(){
			Pair[] deltas = {new Pair(0,1), new Pair(1,0), new Pair(1,1), new Pair(1,-1)};
			for (int i=0;i<size;i++){
				for (int j=0;j<size;j++){
					int tp = t[i][j];
					if (tp == 0) continue;
					for (int d=0;d<4;d++){
						Pair D = deltas[d];
						Pair pos = new Pair(i,j);
						int n = 1;
						for (int k=0;k<size-1;k++){
							pos.x += D.x;
							pos.y += D.y;
							if (pos.x < 0 || pos.x >= size || pos.y<0 || pos.y>=size)
								break;
							int tk = t[pos.x][pos.y];
							if (tk == tp){
								n++;
							}else
								break;
						}
						if (n==size){
							if (tp == 1){
								winner = "X";
							}else{
								winner = "O";
							}
							return true;
						}
					}
				}
			}
			return false;
		}
	}

	
	static interface AI{
		public Pair play(Board b);
	}
	
	static class Pair{
		int x;
		int y;
		Pair(int a, int b){
			x = a; y = b;
		}
		@Override
		public boolean equals(Object b){
			if (b instanceof Pair &&
					x == ((Pair) b).x &&
					y == ((Pair) b).y){
				return true;
			}
			return false;
		}
	}
}
