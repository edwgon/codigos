def cal_bayes(prior_A,prob_B_dado_A,prob_B):
    return(prior_A * prob_B_dado_A) /prob_B

if __name__ == '__main__':
    prob_cancer = 1/100000
    prob_sintoma = 1
    prob_sintoma_dado_no_cancer = 10/99999
    prob_no_cancer = 1 - prob_cancer

    prob_sin = (prob_sintoma* prob_cancer) +(prob_sintoma_dado_no_cancer*prob_no_cancer)

    prob_cancer_sintoma = cal_bayes(prob_cancer,prob_sintoma,prob_sin)

    print(prob_cancer_sintoma)