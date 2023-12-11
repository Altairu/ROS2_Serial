uint8_t send_data[32];
uint8_t receive_data[32];

void setup() {
  Serial.begin(9600);  // シリアル通信の初期化
}

void loop() {
  // データを生成
  for (int i = 0; i < sizeof(send_data); ++i) {
    send_data[i] = i;
  }

  // データをシリアルで送信
  Serial.write(send_data, sizeof(send_data));

  // シリアルからデータを受信
  if (Serial.available() >= sizeof(receive_data)) {
    Serial.readBytes(receive_data, sizeof(receive_data));

    // 受信したデータをそのままLED_BUILTINに出力
    for (int i = 0; i < sizeof(receive_data); ++i) {
      if (receive_data[i] == 1) {
        digitalWrite(LED_BUILTIN, HIGH);
      } else {
        digitalWrite(LED_BUILTIN, LOW);
      }
    }
  }
}
