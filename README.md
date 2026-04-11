<div align="center">

<!-- LOGO / BANNER -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=MathAI%20Calculator&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=Умный%20калькулятор%20с%20высшей%20математикой%20и%20ИИ&descSize=18&descAlignY=60&descColor=c9b6ff" alt="MathAI Calculator Banner"/>

<br/>

[![Stars](https://img.shields.io/github/stars/bositxonn/Calculator?style=for-the-badge&color=302b63&labelColor=0f0c29&logo=github)](https://github.com/bositxonn/Calculator/stargazers)
[![Forks](https://img.shields.io/github/forks/bositxonn/Calculator?style=for-the-badge&color=302b63&labelColor=0f0c29&logo=git)](https://github.com/bositxonn/Calculator/forks)
[![License](https://img.shields.io/github/license/bositxonn/Calculator?style=for-the-badge&color=302b63&labelColor=0f0c29)](LICENSE)
[![Issues](https://img.shields.io/github/issues/bositxonn/Calculator?style=for-the-badge&color=302b63&labelColor=0f0c29)](https://github.com/bositxonn/Calculator/issues)

<br/>

> **MathAI Calculator** — это не просто калькулятор. Это полноценный математический помощник,  
> объединяющий классические вычисления, высшую математику и возможности искусственного интеллекта  
> в одном элегантном интерфейсе.

<br/>

[🚀 Демо](#-демо) · [✨ Функции](#-функции) · [⚙️ Установка](#️-установка) · [📖 Документация](#-использование) · [🤝 Вклад](#-вклад-в-проект)

---

</div>

<br/>

## ✨ Функции

<div align="center">

| Категория | Возможности |
|:---:|:---|
| 🔢 **Базовые вычисления** | Сложение, вычитание, умножение, деление, скобки, проценты |
| 📐 **Тригонометрия** | sin, cos, tan, arcsin, arccos, arctan + гиперболические функции |
| 📈 **Алгебра** | Степени, корни, логарифмы (log, ln, log₂) |
| ∫ **Математический анализ** | Производные, интегралы, пределы, разложения в ряд |
| 🔢 **Матрицы** | Умножение матриц, определитель, обратная матрица, ранг |
| 📊 **Статистика** | Среднее, медиана, дисперсия, стандартное отклонение |
| 🤖 **ИИ-чат** | Объяснение решений, пошаговые вычисления, помощь с задачами |
| 📜 **История** | Сохранение всех вычислений с возможностью экспорта |

</div>

<br/>

## 🤖 ИИ-ассистент

Встроенный чат с искусственным интеллектом — это больше, чем просто ответы на вопросы:

- 💬 **Объясняет решения** — спросите «как решить это уравнение?» и получите пошаговый разбор
- 🧠 **Понимает контекст** — ИИ видит вашу текущую формулу и может работать с ней
- 📝 **Обучающий режим** — просите объяснить теорию, формулы, теоремы
- 🔍 **Проверка работы** — скопируйте задачу, ИИ проверит ваше решение

```
Вы:       "Объясни, как взять производную от sin(x²)"
ИИ:  →    Используем правило цепочки: d/dx[sin(u)] = cos(u)·u',
          где u = x². Тогда u' = 2x.
          Итого: d/dx[sin(x²)] = cos(x²) · 2x
```

<br/>

## ⚙️ Установка

### Требования

- Node.js `>= 18.0` / Python `>= 3.10` *(в зависимости от вашего стека)*
- npm / pip

### Быстрый старт

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/bositxonn/Calculator.git

# 2. Перейдите в папку проекта
cd Calculator

# 3. Установите зависимости
npm install        # или: pip install -r requirements.txt

# 4. Запустите приложение
npm start          # или: python main.py
```

### Переменные окружения

Создайте файл `.env` в корне проекта:

```env
# API ключ для ИИ-чата
AI_API_KEY=your_api_key_here

# Настройки (опционально)
DEFAULT_ANGLE_UNIT=radians   # radians | degrees
DECIMAL_PRECISION=10
```

<br/>

## 📖 Использование

### Базовые вычисления

```
2 + 2 * (3 - 1)   →   6
sqrt(144)          →   12
15% of 200         →   30
```

### Высшая математика

```
# Производная
diff(x^3 + 2x, x)         →   3x² + 2

# Интеграл
integrate(sin(x), x)       →   -cos(x) + C

# Предел
limit((sin(x)/x), x, 0)   →   1

# Матрицы
[[1,2],[3,4]] * [[5,6],[7,8]]  →  [[19,22],[43,50]]
```

### ИИ-чат

Просто введите вопрос на естественном языке:

```
"Помоги решить систему уравнений: x+y=5, 2x-y=1"
"Что такое интеграл и зачем он нужен?"
"Проверь моё решение: ..."
```

<br/>

## 🏗️ Архитектура

```
📦 MathAI Calculator
├── 🧮 core/
│   ├── parser.js          # Парсинг математических выражений
│   ├── evaluator.js       # Вычисление выражений
│   └── higher-math/
│       ├── calculus.js    # Производные и интегралы
│       ├── matrices.js    # Матричные операции
│       └── statistics.js  # Статистика
├── 🤖 ai/
│   ├── chat.js            # ИИ-чат
│   └── context.js         # Контекст вычислений для ИИ
├── 🎨 ui/
│   ├── components/        # UI компоненты
│   └── themes/            # Темы оформления
└── 📜 history/
    └── storage.js         # История вычислений
```

<br/>

## 🛠️ Технологии

<div align="center">

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

</div>

*(замените на реальные технологии вашего проекта)*

<br/>

## 🗺️ Планы развития

- [x] Базовые арифметические операции
- [x] Тригонометрические функции
- [x] Матричные вычисления
- [x] ИИ-чат ассистент
- [ ] 📱 Мобильное приложение (iOS / Android)
- [ ] 📊 Построение графиков функций
- [ ] 🌐 Веб-версия (PWA)
- [ ] 🔗 Общий доступ к вычислениям по ссылке
- [ ] 🎙️ Голосовой ввод формул

<br/>

## 🤝 Вклад в проект

Вклад приветствуется! Вот как можно помочь:

1. 🍴 Сделайте **Fork** репозитория
2. 🌿 Создайте ветку: `git checkout -b feature/amazing-feature`
3. 💾 Зафиксируйте изменения: `git commit -m 'Add amazing feature'`
4. 📤 Отправьте ветку: `git push origin feature/amazing-feature`
5. 🔃 Откройте **Pull Request**

Перед тем как вносить вклад, ознакомьтесь с [CONTRIBUTING.md](CONTRIBUTING.md).

<br/>

## 📄 Лицензия

Распространяется под лицензией **MIT**. Подробности в файле [LICENSE](LICENSE).

<br/>

## 🙏 Благодарности

- [Math.js](https://mathjs.org/) — мощная математическая библиотека
- [OpenAI](https://openai.com/) — API для ИИ-чата
- Все контрибьюторы, которые помогают улучшать проект ❤️

<br/>

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=100&section=footer" alt="footer"/>

**Сделано с ❤️ и ∞ математики**

⭐ Если проект понравился — не забудьте поставить звезду!

</div>
