```Java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;
public class MultipleStageDemo extends Application {
  @Override // Override the start method in the Application class
  public void start(Stage primaryStage) {
    // Create a scene and place a button in the scene
    Scene scene = new Scene(new Button("OK"), 200, 250);
    primaryStage.setTitle("MyJavaFX"); // Set the stage title
    primaryStage.setScene(scene); // Place the scene in the stage
    primaryStage.show(); // Display the stage
    Stage stage = new Stage(); // Create a new stage
    stage.setTitle("Second Stage"); // Set the stage title
    // Set a scene with a button in the stage
    stage.setScene(new Scene(new Button("New Stage"), 200, 250));        
    stage.show(); // Display the stage
  }
  
  /**
   * The main method is only needed for the IDE with limited
   * JavaFX support. Not needed for running from the command line.
   */
  public static void main(String[] args) {
    launch(args);
  }
}
a. Container
b. Control
c. Shape
d. 
e. ImageView
StackPnae
a. Bisa membuat beberapa stage dalam 1 aplikasi namun yang menjadi stage primer hanya 1, yang diconstruct pada aplikasi
Buatlah aplikasi sederhana sesuai UI yang dilampirkan dan ketentuan sudah ada di assignment topik "JavaFX" (minggu lalu). Aplikasi harus membaca data di dataset.txt. Submit ZIP file *.java dari class-class yang kalian buat. Jika ada penambahan pada dataset.txt, masukkan juga ke dalam ZIP file.
PASTIKAN bisa dijalankan (tidak error) dan TIDAK PLAGIAT!
Yang menjadi kebutuhan dari latihan ini cukup sebagai berikut:
- Scene 1 (Latihan JavaFX_1.png): User memasukkan norek dan klik "Lanjut". Jika norek tidak ada di dataset.txt, jangan pindah Scene. (Silakan jika ingin berkreasi dengan modal/popup yang memunculkan informsi norek tidak ada)
- Scene 2 (Latihan JavaFX_2.png): Jika user klik "Jangka Waktu", UI menampilkan isian tanggal awal dan akhir.
- Scene 2 (Latihan JavaFX_3.png): Jika user klik "Periode", UI menampilkan opsi "1 Bulan Terakhir", "1 Minggu Terakhir", "Hari Ini".
- opsi "Jangka Waktu" dan "Periode" BOLEH pakai TabPane ya :)
- Scene 2 (Latihan JavaFX_4.png): User klik "1 Bulan Terakhir", lalu klik "Lanjut".
- Scene 3 (Latihan JavaFX_5.png): Aplikasi menampilkan daftar transaksi sesuai rekening saja, TIDAK perlu cek tanggal untuk latihan kali ini. Kalian bisa pakai TableView.
- Menampilkan transaksi untuk "1 minggu terakhir" ataupun "hari ini" TIDAK WAJIB, namun silakan jika ingin berkreasi. Jika kalian mau menambah dataset sehingga lebih real dan untuk berkreasi, dipersilakan :)
Di luar poin yang diminta di atas, silakan jika ingin menambahkan fungsionalitas lain (seperti "Kembali" misalnya ke halaman awal atau exit, atau filter transaksi berdasarkan "Jangka Waktu" dan lain-lain). Penggunaan style saya bebaskan, asalkan ada pembeda antara Button yang di-select dan yang tidak.
Selamat meng-eksplore JavaFX!
N.B. latihan implementasi ini murni sekadar latihan dan hanya masuk ke nilai bonus (bukan nilai tugas/lab/kuis/ujian). Silakan dimanfaatkan untuk melatih skill Java.
when you got something, you build your own jail
```