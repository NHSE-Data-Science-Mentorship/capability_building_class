def clean_ecds(ecds_df):
    ecds_df = ecds_df.loc[(ecds_df['sex'] == '1') | (ecds_df['sex'] == '2'), :]
    ecds_df.loc[:, 'age_at_arrival'] = ecds_df['age_at_arrival'].astype('float')
    ecds_df.loc[:, 'sex'] = ecds_df['sex'].astype('category')
    ecds_df.loc[:, 'admitted'] = ecds_df['admitted'].astype('float')

    return ecds_df


def split_features_targets(ecds_df):
    feature_df = ecds_df.loc[:, ['age_at_arrival', 'sex']]
    target_df = ecds_df.loc[:, ['admitted']]

    return feature_df, target_df
