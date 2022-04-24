import { Avatar, Box, Card, CardContent, Grid, Typography } from '@mui/material';
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';
import PeopleIcon from '@mui/icons-material/PeopleOutlined';
import { Button } from '@mui/material';

export const TotalCustomers = (props) => (
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
            SIZE OF POTENTIAL FIELDS FOR SOLAR FARMING
          </Typography>
          <Typography
            color="textPrimary"
            variant="h4"
          >
            1,6k hectares
          </Typography>
           <Button variant="contained" onClick={(e) => {
                                                               e.preventDefault();
                                                               window.location.href='/sunlight.html';
                                                               }}
                                                         >View our dashboard</Button>
        </Grid>
        <Grid item>
          <Avatar
            sx={{
              backgroundColor: 'success.main',
              height: 56,
              width: 56
            }}
          >
          </Avatar>
        </Grid>
      </Grid>
    </CardContent>
  </Card>
);
