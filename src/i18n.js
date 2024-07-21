import { createI18n } from "vue-i18n";

const messages = {
  en: {
    welcome: "Welcome to the Crypto Mining Bot!",
  },
  fr: {
    welcome: "Bienvenue dans le bot de minage de cryptomonnaie!",
  },
};

const i18n = createI18n({
  locale: "en",
  messages,
});

export default i18n;
