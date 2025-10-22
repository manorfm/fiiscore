from src.domain.model.fii import FII
import math

class FundamentalAnalysisService:
    def __init__(self, weights: dict = None):
        if weights is None:
            # Pesos ajustados para uma análise balanceada
            self.weights = {
                'dividend_yield': 0.30,
                'pvp': 0.25,
                'vacancy': 0.20,
                'liquidity': 0.15,
                'asset_amount': 0.10,
            }
        else:
            self.weights = weights

    def get_analysis(self, fii: FII) -> dict:
        """
        Executa a análise fundamentalista completa, retornando o score e a classificação.
        """
        score = self.calculate_score(fii)
        classification = self._classify(score)
        return {"score": score, "classification": classification}

    def calculate_score(self, fii: FII) -> float:
        """
        Calcula o score normalizado com base nas métricas do FII.
        """
        scores = {
            'dividend_yield': self._normalize_dividend_yield(fii.dividendYield),
            'pvp': self._normalize_pvp(fii.pvp),
            'vacancy': self._normalize_vacancy(fii.vacancy),
            'liquidity': self._normalize_liquidity(fii.daily_liquidity),
            'asset_amount': self._normalize_asset_amount(fii.asset_amount),
        }

        final_score = (
            scores['dividend_yield'] * self.weights['dividend_yield'] +
            scores['pvp'] * self.weights['pvp'] +
            scores['vacancy'] * self.weights['vacancy'] +
            scores['liquidity'] * self.weights['liquidity'] +
            scores['asset_amount'] * self.weights['asset_amount']
        )

        return round(final_score, 4)

    def _classify(self, score: float) -> str:
        """
        Classifica um FII com base no seu score final.
        """
        if score > 0.75:
            return "Recomendado"
        elif score > 0.5:
            return "Neutro"
        else:
            return "Não Recomendado"

    # --- Funções de Normalização (0 a 1) ---

    def _normalize_dividend_yield(self, dy: float) -> float:
        """
        Normaliza o dividend yield. Considera 1.2% (0.012) como nota máxima.
        """
        target_dy = 0.012  # 1.2%
        if target_dy == 0: return 1.0 # Avoid division by zero, treat as neutral
        # Capado em 1.25 para evitar distorções
        return min(dy / target_dy, 1.25)

    def _normalize_pvp(self, pvp: float) -> float:
        # PVP ideal é < 1.0. Um PVP de 1.1 é neutro (0.5), acima disso é ruim.
        # Usamos uma função sigmoide invertida para uma normalização mais suave.
        if pvp <= 0: return 0
        return 1 / (1 + math.exp(10 * (pvp - 1.1)))

    def _normalize_vacancy(self, vacancy: float) -> float:
        # Vacância de 0% é nota 1.0. Acima de 20% é nota 0.
        return max(0, 1 - (vacancy / 0.20))

    def _normalize_liquidity(self, liquidity: float) -> float:
        # Acima de 1M de liquidez é nota 1.0. Abaixo de 100k é nota 0.
        if liquidity >= 1_000_000: return 1.0
        if liquidity <= 100_000: return 0.0
        return (liquidity - 100_000) / (1_000_000 - 100_000)

    def _normalize_asset_amount(self, amount: int) -> float:
        # Acima de 10 ativos (diversificação alta) é nota 1.0. 1 ativo é 0.1.
        if amount >= 10: return 1.0
        if amount <= 1: return 0.1
        return (amount - 1) / (10 - 1)
