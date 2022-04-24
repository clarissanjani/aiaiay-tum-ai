import { Avatar, Box, Card, CardContent, Grid, Typography } from '@mui/material';
import ArrowDownwardIcon from '@mui/icons-material/ArrowDownward';
import TungstenIcon from '@mui/icons-material/Tungsten';
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';

export const Budget = (props) => (
  <Card {...props}>
    <CardContent>
      <Grid
        container
        spacing={3}
        sx={{ justifyContent: 'space-between' }}
      >
        <Grid item>
          <Typography
            color="textSecondary"
            gutterBottom
            variant="overline"
          >
            Yearly Electricty from Renewable Sources
          </Typography>
          <Typography
            color="textPrimary"
            variant="h4"
          >
            2,9 Billion kWh
          </Typography>
        </Grid>
        <Grid item>
          <Avatar
            sx={{
              backgroundColor: 'success.main',
              height: 56,
              width: 56
            }}
          >
            <TungstenIcon />
          </Avatar>
        </Grid>
      </Grid>
      <Box
        sx={{
          alignItems: 'center',
          display: 'flex',
          pt: 2
        }}
      >
        <ArrowUpwardIcon color="success" />
        <Typography
          variant="body2"
          sx={{
            mr: 1
          }}
        >
          14,5%
        </Typography>
        <Typography
          color="textSecondary"
          variant="caption"
        >
          Since last layer
        </Typography>
      </Box>
    </CardContent>
  </Card>
);

