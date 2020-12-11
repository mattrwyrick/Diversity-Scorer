from diverstudio.tools import ScoringAid


class SimpleScore(ScoringAid):

    def __init__(self, pv_attrs, target_keys, employee):
        ScoringAid.__init__(self, pv_attrs, target_keys, employee)
        self.score = self._score()

    def _score(self):
        """
        Return the score of the actual distribution vs the target distribution % differences summed together then / 2
        :return:
        """
        total = 0
        for key in self.target_distribution:
            a_value = self.actual_distribution[key]
            t_value = self.target_distribution[key]
            total += abs(a_value - t_value)

        return total / 2


class SimpleChiSqrScore(ScoringAid):

    def __init__(self, pv_attrs, target_keys, employee):
        ScoringAid.__init__(self, pv_attrs, target_keys, employee)
        self.score = self._score()

    def _score(self):
        """
        Return the p value for the observed chi square test (observed organization vs the target organization)
        :return:
        """
        from scipy.stats import chi2_contingency
        from scipy.stats import chi2

        actual_list = []
        target_list = []
        for key in self.target_distribution:
            actual_list.append(self.actual_distribution[key]*100)
            target_list.append(self.target_distribution[key]*100)

        table = [actual_list, target_list]
        stat, p, dof, expected = chi2_contingency(table)

        # Test Statistic
        prob = 0.95
        critical = chi2.ppf(prob, dof)
        if abs(stat) >= critical:
            ts_value = f"Test Stat:{abs(stat)}:{critical}:Dependent"
        else:
            ts_value = f"{abs(stat)}:{critical}:Independent"

        # interpret p-value
        alpha = 1.0 - prob
        if p <= alpha:
            p_value = f"P Value:{p}:{alpha}:Dependent"
        else:
            p_value = f"P Value:{p}:{alpha}:Independent"

        return round(p, 5)












