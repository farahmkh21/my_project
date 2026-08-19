/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: fkhaldi <fkhaldi@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*                                                     #+#    #+#             */
/*                                                    ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "get_next_line.h"

static int	ft_get_line(char **stach, char **line)
{
	char	*nl;
	char	*tmp;

	if (!stach || !*stach || !**stach)
		return (0);
	nl = ft_strchr(*stach, '\n');
	if (!nl)
		return (0);
	*line = ft_substr(*stach, 0, (nl - *stach) + 1);
	if (!*line)
		return (-1);
	tmp = *stach;
	*stach = ft_strdup(nl + 1);
	free(tmp);
	if (!*stach)
	{
		free(*line);
		*line = NULL;
		return (-1);
	}
	return (1);
}

static int	ft_read_and_store(int fd, char **stach)
{
	char	*buf;
	char	*tmp;
	int		bytes;

	buf = malloc((size_t)BUFFER_SIZE + 1);
	if (!buf)
		return (-1);
	bytes = read(fd, buf, BUFFER_SIZE);
	if (bytes <= 0)
	{
		free(buf);
		return (bytes);
	}
	buf[bytes] = '\0';
	if (!*stach)
		*stach = ft_strdup("");
	if (!*stach)
		return (free(buf), -1);
	tmp = ft_strjoin(*stach, buf);
	free(*stach);
	free(buf);
	*stach = tmp;
	return (1);
}

static char	*ft_get_final_line(char **stach)
{
	char	*line;

	if (!stach || !*stach || **stach == '\0')
	{
		free(*stach);
		*stach = NULL;
		return (NULL);
	}
	line = ft_strdup(*stach);
	free(*stach);
	*stach = NULL;
	return (line);
}

char	*get_next_line(int fd)
{
	static char	*stach;
	char		*line;
	int			cond;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	cond = 1;
	while (cond > 0 && !ft_strchr(stach, '\n'))
		cond = ft_read_and_store(fd, &stach);
	if (cond == -1)
	{
		free(stach);
		stach = NULL;
		return (NULL);
	}
	line = NULL;
	if (ft_get_line(&stach, &line) == 1)
		return (line);
	return (ft_get_final_line(&stach));
}
