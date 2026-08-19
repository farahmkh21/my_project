/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: fkhaldi <fkhaldi@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*                                                     #+#    #+#             */
/*                                                    ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*dublicate_ptr;
	size_t	len;

	len = ft_strlen (s) + 1;
	dublicate_ptr = (char *) malloc (len);
	if (dublicate_ptr == NULL)
		return (NULL);
	ft_memcpy(dublicate_ptr, s, len);
	return (dublicate_ptr);
}
