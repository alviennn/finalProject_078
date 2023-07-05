#include <iostream>
using namespace std;

class bidangDatar {
private:
	int x, y;
public:
	bidangDatar() {
		x = 0;
		y = 0;
	}
	virtual void input() {}
	virtual float Luas(int a) { return 0; }
	virtual float Keliling(int a) { return 0; }
	virtual void cekUkuran() { return; }

	void setX(int a) {
		this->x = a;
	}
	void setY(int b) {
		this->y = b;
	}
	int getX() {
		return x;
	}
	int getY() {
		return y;
	}
};

class Lingkaran :public bidangDatar {
public:
	void input() {
		cout << "Masukkan jari-jarinya: ";
		int x;
		cin >> x;
		setX(x);
		cout << "Luas Lingkaran = " << Luas() << endl;
		cout << "Keliling Lingkaran = " << Keliling() << endl;
		cout << "Ukuran lingkaran adalah ";
		cekUkuran();
	}
	float Luas() {
		return (3.14 * getX() * getX());
	}
	float Keliling() {
		return (2 * 3.14 * getX());
	}
	void cekUkuran() {
		if (getX() < 10) {
			cout << "kecil" << endl;
		}
		else if (getX() < 20) {
			cout << "sedang" << endl;
		}
		else if (getX() > 40) {
			cout << "besar" << endl;
		}
	}
};

class Persegipanjang :public bidangDatar {
public:
	void input() {
		cout << "Masukkan panjang: ";
		int x;
		cin >> x;
		setX(x);
		cout << "Masukkan lebar: ";
		int y;
		cin >> y;
		setY(y);
		cout << "Luas persegi panjang = " << Luas() << endl;
		cout << "Keliling persegi panjang = " << Keliling() << endl;
		cout << "Ukuran persegi panjang adalah ";
		cekUkuran();
	}
	float Luas() {
		return (getX() * getY());
	}
	float Keliling() {
		return (2 *(getX() * getY()));
	}

	void cekUkuran() {
		if (getX() < 10 && getY() < 10) {
			cout << "kecil" << endl;
		}
		else if (getX() < 20 && getY() < 20) {
			cout << "sedang" << endl;
		}
		else if (getX() > 40 && getY() > 40) {
			cout << "besar" << endl;
		}
	}
};

int main() {
	bidangDatar* ob;
	char ch;

	do {
		cout << "Lingkaran dibuat" << endl;
		ob = new Lingkaran;
		ob->input();
		cout << "Persegi Panjang dibuat" << endl;
		ob = new Persegipanjang;
		ob->input();

		cout << "Apakah anda ingin mengulang program? (y/n): ";
		cin >> ch;

		delete ob;

	} while (ch == 'y' || ch == 'Y');
	return 0;
}