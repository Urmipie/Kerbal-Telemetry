import time
def langChooser():
    print("Please choose a language:")
    print("1: English")
    print("2: Pусский")
    print("3: 中文")
    print("4: Türkçe")
    print("5: Français")
    print("6: Español")
    print("7: 日本語")
    print("8: Український")
    lang = input("> ")
    refreshRate = 0
    chartRate = 0
    print("")
    if lang == "1":  # English
        print("Web interface language is now selected as English.")
        print("Refresh rate and chart refresh rate are settings which will affect the performance of the program.")
        print("Higher you set these values, lighter the program will be.")
        print("Lower you set these values, it gets close to being more 'real-time'.")
        print("Please enter only numbers which you want to set:")
        refRateSet = False
        while refRateSet == False:
            try:
                print("")
                print("Please set the refresh rate for the program (default: 200ms)")
                refreshRate = input("Refresh Rate> ")
                refreshRate = 200 if refreshRate=="" else int(refreshRate)
                if refreshRate < 0:
                    raise ValueError
                refRateSet = True
            except ValueError:
                print("Please enter a valid number.")
        chartRefSet = False
        while chartRefSet == False:
            try:
                print("")
                print("Please set the chart refresh rate for the program (default: 1200ms)")
                chartRate = input("Chart Refresh Rate> ")
                chartRate = 1200 if chartRate=="" else int(chartRate)
                if chartRate < 0:
                    raise ValueError
                chartRefSet = True
            except ValueError:
                print("Please enter a valid number.")
        with open("static/refreshRate.json", "w") as f:
            f.write('{"refreshRate":'+str(refreshRate)+', "chartsRate": '+str(chartRate)+', "lang": "en"}')
        print("Settings saved successfully. Please restart the web interface.")
        time.sleep(3.5)
    elif lang == "2":  # Russian
        print("Язык интерфейса выбран как русский.")
        print("Обновить скорость и частоту обновления диаграммы - эти настройки влияют на производительность программы.")
        print("Чем выше вы устанавливаете эти значения, тем  легче программе будет работать")
        print("Понижая  эти значения, программа будет лучше работать  «в режиме реального времени».")
        print("Пожалуйста, введите только те числа, которые вы хотите установить:")
        refRateSet = False
        while refRateSet == False:
            try:
                print("")
                print("Установите частоту обновления для программы (по умолчанию: 200 мс)")
                refreshRate = input("Частота обновления> ")
                refreshRate = 200 if refreshRate=="" else int(refreshRate)
                if refreshRate < 0:
                    raise ValueError
                refRateSet = True
            except ValueError:
                print("Пожалуйста, введите корректное число.")
        chartRefSet = False
        while chartRefSet == False:
            try:
                print("")
                print("Установите частоту обновления графика для программы (по умолчанию: 1200 мс)")
                chartRate = input("Частота обновления диаграммы> ")
                chartRate = 1200 if chartRate=="" else int(chartRate)
                if chartRate < 0:
                    raise ValueError
                chartRefSet = True
            except ValueError:
                print("Пожалуйста, введите корректное число.")
        with open("static/refreshRate.json", "w") as f:
            f.write('{"refreshRate":'+str(refreshRate)+', "chartsRate": '+str(chartRate)+', "lang": "ru"}')
        print("Настройки успешно сохранены. Пожалуйста, перезапустите веб-интерфейс.")
        time.sleep(3.5)
    elif lang == "3":  # Chinese
        print("界面语言现已选择为中文。")
        print("刷新率和图表刷新率是会影响程序性能的设置")
        print("这些值设置得越高，程序就越轻。")
        print("将这些值设置得越低，它就越接近于“实时”。")
        print("请仅输入您要设置的数字：")
        refRateSet = False
        while refRateSet == False:
            try:
                print("")
                print("请设置程序的刷新率（默认值：200ms")
                refreshRate = input("刷新率> ")
                refreshRate = 100 if refreshRate=="" else int(refreshRate)
                if refreshRate < 0:
                    raise ValueError
                refRateSet = True
            except ValueError:
                print("请输入一个有效的数字。")
        chartRefSet = False
        while chartRefSet == False:
            try:
                print("")
                print("请为程序设置图表刷新率（默认值：1200ms）")
                chartRate = input("图表刷新率> ")
                chartRate = 1200 if chartRate=="" else int(chartRate)
                if chartRate < 0:
                    raise ValueError
                chartRefSet = True
            except ValueError:
                print("请输入一个有效的数字。")
        with open("static/refreshRate.json", "w") as f:
            f.write('{"refreshRate":'+str(refreshRate)+', "chartsRate": '+str(chartRate)+', "lang": "zh"}')
        print("设置已成功保存。 请重新启动界面。")
        time.sleep(3.5)
    elif lang == "4":  # Turkish
        print("Arayüz dili Türkçe olarak seçildi.")
        print("Yenileme hızı ve grafik yenileme hızı programın çalışma performansını etkileyen ayarlardır.")
        print("Bu değerleri ne kadar yüksek ayarlarsanız, program o kadar hafif çalışır.")
        print("Ancak ne kadar düşük ayarlarsanız, o kadar 'gerçek zamanlı' olur.")
        print("Lütfen seçmek istediğinizi sayı ile giriniz:")
        refRateSet = False
        while refRateSet == False:
            try:
                print("")
                print("Lütfen programın yenileme hızını girin (varsayılan: 200ms)")
                refreshRate = input("Yenileme Hızı> ")
                refreshRate = 200 if refreshRate=="" else int(refreshRate)
                if refreshRate < 0:
                    raise ValueError
                refRateSet = True
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        chartRefSet = False
        while chartRefSet == False:
            try:
                print("")
                print("Lütfen grafik yenileme hızını girin (varsayılan: 1200ms)")
                chartRate = input("Grafik Yenileme Hızı> ")
                chartRate = 1200 if chartRate=="" else int(chartRate)
                if chartRate < 0:
                    raise ValueError
                chartRefSet = True
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        with open("static/refreshRate.json", "w") as f:
            f.write('{"refreshRate":'+str(refreshRate)+', "chartsRate": '+str(chartRate)+', "lang": "tr"}')
        print("Ayarlar başarıyla uygulandı. Lütfen web arayüzünü yeniden başlatın.")
        time.sleep(3.5)
    elif lang == "5":  # French
        print("La langue de l'interface Web est maintenant sélectionnée en français.")
        print("Le taux de rafraîchissement et le taux de rafraîchissement du graphique sont des paramètres qui affecteront les performances du programme.")
        print("Plus vous élevez ces valeurs, moins le programme ralentira votre ordinateur.")
        print("Si vous diminuez ces valeurs, le programme sera plus proche du \"temps réel\".")
        print("Veuillez n'entrer que des nombres que vous souhaitez définir:")
        refRateSet = False
        while refRateSet == False:
            try:
                print("")
                print("Veuillez définir la fréquence de rafraîchissement du programme (par défaut: 200 ms)")
                refreshRate = input("Fréquence de rafraîchissement> ")
                refreshRate = 200 if refreshRate=="" else int(refreshRate)
                if refreshRate < 0:
                    raise ValueError
                refRateSet = True
            except ValueError:
                print("S'il vous plait, entrez un nombre valide.")
        chartRefSet = False
        while chartRefSet == False:
            try:
                print("")
                print("Veuillez définir le taux de rafraîchissement du graphique pour le programme (par défaut: 1200 ms)")
                chartRate = input("Taux de rafraîchissement du graphique> ")
                chartRate = 1200 if chartRate=="" else int(chartRate)
                if chartRate < 0:
                    raise ValueError
                chartRefSet = True
            except ValueError:
                print("S'il vous plait, entrez un nombre valide.")
        with open("static/refreshRate.json", "w") as f:
            f.write('{"refreshRate":'+str(refreshRate)+', "chartsRate": '+str(chartRate)+', "lang": "fr"}')
        print("Paramètres enregistrés avec succès. Veuillez redémarrer l'interface Web.")
        time.sleep(3.5)
    elif lang == "6":  # Spanish
        print("El idioma de la interfaz web ahora está seleccionado como español.")
        print("La frecuencia de actualización y la frecuencia de actualización del gráfico son configuraciones que afectarán el rendimiento del programa.")
        print("Cuanto más altos establezca estos valores, más ligero será el programa.")
        print("Cuanto más bajo establezca estos valores, se acerca a ser más \"en tiempo real\".")
        print("Ingrese solo los números que desee configurar:")
        refRateSet = False
        while refRateSet == False:
            try:
                print("")
                print("Establezca la frecuencia de actualización del programa (predeterminado: 200 ms)")
                refreshRate = input("Frecuencia de actualización> ")
                refreshRate = 200 if refreshRate=="" else int(refreshRate)
                if refreshRate < 0:
                    raise ValueError
                refRateSet = True
            except ValueError:
                print("Por favor ingrese un número valido.")
        chartRefSet = False
        while chartRefSet == False:
            try:
                print("")
                print("Configure la frecuencia de actualización del gráfico para el programa (predeterminado: 1200 ms)")
                chartRate = input("Tasa de actualización del gráfico> ")
                chartRate = 1200 if chartRate=="" else int(chartRate)
                if chartRate < 0:
                    raise ValueError
                chartRefSet = True
            except ValueError:
                print("Por favor ingrese un número valido.")
        with open("static/refreshRate.json", "w") as f:
            f.write('{"refreshRate":'+str(refreshRate)+', "chartsRate": '+str(chartRate)+', "lang": "es"}')
        print("La configuración se ha guardado correctamente. Reinicie la interfaz web.")
        time.sleep(3.5)
    elif lang == "7":  # Japanese
        print("Webインターフェイス言語が日本語として選択されるようになりました。")
        print("リフレッシュレートとチャートのリフレッシュレートは、プログラムのパフォーマンスに影響を与える設定です。")
        print("これらの値を高く設定すると、プログラムは軽くなります。")
        print("これらの値を低く設定すると、より「リアルタイム」に近くなります。")
        print("設定したい番号のみを入力してください：")
        refRateSet = False
        while refRateSet == False:
            try:
                print("")
                print("プログラムのリフレッシュレートを設定してください（デフォルト：200ms）")
                refreshRate = input("リフレッシュレート> ")
                refreshRate = 200 if refreshRate=="" else int(refreshRate)
                if refreshRate < 0:
                    raise ValueError
                refRateSet = True
            except ValueError:
                print("有効な数値を入力してください。")
        chartRefSet = False
        while chartRefSet == False:
            try:
                print("")
                print("プログラムのチャートリフレッシュレートを設定してください（デフォルト：1200ms）")
                chartRate = input("チャートのリフレッシュレート> ")
                chartRate = 1200 if chartRate=="" else int(chartRate)
                if chartRate < 0:
                    raise ValueError
                chartRefSet = True
            except ValueError:
                print("有効な数値を入力してください。")
        with open("static/refreshRate.json", "w") as f:
            f.write('{"refreshRate":'+str(refreshRate)+', "chartsRate": '+str(chartRate)+', "lang": "jp"}')
        print("設定が正常に保存されました。 Webインターフェイスを再起動してください。")
        time.sleep(3.5)
    elif lang == "8":  # Ukrainian
        print("Мова веб - інтерфейсу тепер обраний як англійська.")
        print("Частота оновлення і частота оновлення графіка-це налаштування, які будуть впливати на продуктивність програми.")
        print("Чим вище ви встановите це значення, тим легше буде програма.")
        print("Чим нижче ви встановлюєте ці значення, тим ближче він стає до \"реального часу\".")
        print("Будь ласка, введіть тільки ті номери, які ви хочете встановити:")
        refRateSet = False
        while refRateSet == False:
            try:
                print("")
                print("Будь ласка, встановіть частоту оновлення програми (за замовчуванням: 200 мс)")
                refreshRate = input("Частота Поновлення> ")
                refreshRate = 200 if refreshRate=="" else int(refreshRate)
                if refreshRate < 0:
                    raise ValueError
                refRateSet = True
            except ValueError:
                print("Будь ласка, введіть дійсний номер.")
        chartRefSet = False
        while chartRefSet == False:
            try:
                print("")
                print("Будь ласка, встановіть частоту оновлення графіка для програми (за замовчуванням: 1200 мс)")
                chartRate = input("Частота оновлення графіка> ")
                chartRate = 1200 if chartRate=="" else int(chartRate)
                if chartRate < 0:
                    raise ValueError
                chartRefSet = True
            except ValueError:
                print("Будь ласка, введіть дійсний номер.")
        with open("static/refreshRate.json", "w") as f:
            f.write('{"refreshRate":'+str(refreshRate)+', "chartsRate": '+str(chartRate)+', "lang": "uk"}')
        print("Налаштування успішно збережено. Будь ласка, перезавантажте веб-інтерфейс.")
        time.sleep(3.5)
    with open("firststart.cfg", "w") as f:
        f.write("1")

if __name__ == "__main__":
    langChooser()
